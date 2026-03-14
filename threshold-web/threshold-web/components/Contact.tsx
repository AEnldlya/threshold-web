'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { useForm } from 'react-hook-form'

type FormData = {
  name: string
  email: string
  phone: string
  business: string
  businessType: string
  message: string
}

export default function Contact() {
  const { register, handleSubmit, formState: { errors, isSubmitting }, reset, watch } = useForm<FormData>()
  const [submitted, setSubmitted] = useState(false)
  const [submitError, setSubmitError] = useState<string | null>(null)
  const formValues = watch()
  const filledFields = Object.values(formValues).filter(Boolean).length

  const onSubmit = async (data: FormData) => {
    try {
      setSubmitError(null)
      // In production, this would send to your backend
      console.log('Form submitted:', data)
      
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      setSubmitted(true)
      reset()
      
      // Hide success message after 6 seconds
      setTimeout(() => setSubmitted(false), 6000)
    } catch (error) {
      setSubmitError('Failed to submit. Please try again.')
    }
  }

  return (
    <section id="contact" className="section-padding bg-gradient-to-b from-slate-50 to-white relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-0 right-0 w-96 h-96 bg-blue-100/20 rounded-full filter blur-3xl -z-10"></div>
      <div className="absolute bottom-20 left-0 w-80 h-80 bg-cyan-100/20 rounded-full filter blur-3xl -z-10"></div>

      <div className="container-max max-w-4xl">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '0px 0px -200px 0px' }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <span className="inline-block px-4 py-2 rounded-full bg-blue-100/80 text-blue-700 text-sm font-medium mb-6 border border-blue-200/50">
            Get Started Today
          </span>
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Ready to Build Your Website?
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
            Let's talk about your project. Call or fill out the form below, and we'll get back to you within 24 hours.
          </p>
        </motion.div>

        {/* Two column layout */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12 mb-12">
          {/* Contact info */}
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: '0px 0px -150px 0px' }}
            transition={{ duration: 0.8 }}
            className="lg:col-span-1 space-y-8"
          >
            {/* Phone */}
            <div className="group p-6 rounded-xl bg-white border border-slate-200/50 hover:border-blue-300/50 hover:shadow-lg transition-all duration-300">
              <div className="flex items-center gap-4 mb-2">
                <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white">
                  ☎️
                </div>
                <h3 className="font-semibold text-slate-900">Call Us</h3>
              </div>
              <a href="tel:6033067508" className="text-xl font-bold text-blue-600 hover:text-blue-700 transition-colors">
                603-306-7508
              </a>
              <p className="text-sm text-slate-600 mt-2">Call or text anytime</p>
            </div>

            {/* Email */}
            <div className="group p-6 rounded-xl bg-white border border-slate-200/50 hover:border-blue-300/50 hover:shadow-lg transition-all duration-300">
              <div className="flex items-center gap-4 mb-2">
                <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white">
                  ✉️
                </div>
                <h3 className="font-semibold text-slate-900">Email</h3>
              </div>
              <a href="mailto:hello@thresholdweb.com" className="text-lg font-bold text-blue-600 hover:text-blue-700 transition-colors break-all">
                hello@thresholdweb.com
              </a>
              <p className="text-sm text-slate-600 mt-2">We respond within 24 hours</p>
            </div>

            {/* Response time */}
            <div className="p-6 rounded-xl bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200/50">
              <p className="text-sm font-medium text-slate-600 mb-3">
                <span className="inline-flex items-center gap-2">
                  <span className="relative flex h-2 w-2">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-500 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                  </span>
                  Quick Responses
                </span>
              </p>
              <p className="text-sm text-slate-700 font-medium">
                We typically respond within 1-2 hours during business hours.
              </p>
            </div>
          </motion.div>

          {/* Form */}
          <motion.div
            initial={{ opacity: 0, x: 40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: '0px 0px -150px 0px' }}
            transition={{ duration: 0.8 }}
            className="lg:col-span-2"
          >
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
              {/* Name and Email */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <label className="block text-sm font-semibold text-slate-900">
                    Full Name <span className="text-red-500">*</span>
                  </label>
                  <input
                    {...register('name', { required: 'Name is required' })}
                    type="text"
                    className="input-field"
                    placeholder="John Smith"
                    autoComplete="name"
                  />
                  {errors.name && (
                    <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-red-500 text-sm">
                      {errors.name.message}
                    </motion.span>
                  )}
                </div>

                <div className="space-y-2">
                  <label className="block text-sm font-semibold text-slate-900">
                    Email <span className="text-red-500">*</span>
                  </label>
                  <input
                    {...register('email', {
                      required: 'Email is required',
                      pattern: { value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i, message: 'Invalid email' }
                    })}
                    type="email"
                    className="input-field"
                    placeholder="john@company.com"
                    autoComplete="email"
                  />
                  {errors.email && (
                    <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-red-500 text-sm">
                      {errors.email.message}
                    </motion.span>
                  )}
                </div>
              </div>

              {/* Phone and Business Type */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <label className="block text-sm font-semibold text-slate-900">
                    Phone <span className="text-red-500">*</span>
                  </label>
                  <input
                    {...register('phone', { required: 'Phone is required' })}
                    type="tel"
                    className="input-field"
                    placeholder="(603) 306-7508"
                    autoComplete="tel"
                  />
                  {errors.phone && (
                    <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-red-500 text-sm">
                      {errors.phone.message}
                    </motion.span>
                  )}
                </div>

                <div className="space-y-2">
                  <label className="block text-sm font-semibold text-slate-900">
                    Business Type
                  </label>
                  <select
                    {...register('businessType')}
                    className="input-field"
                  >
                    <option value="">Select an option</option>
                    <option value="salon">Hair Salon</option>
                    <option value="restaurant">Restaurant</option>
                    <option value="service">Service Business</option>
                    <option value="retail">Retail</option>
                    <option value="other">Other</option>
                  </select>
                </div>
              </div>

              {/* Business Name */}
              <div className="space-y-2">
                <label className="block text-sm font-semibold text-slate-900">
                  Business Name <span className="text-red-500">*</span>
                </label>
                <input
                  {...register('business', { required: 'Business name is required' })}
                  type="text"
                  className="input-field"
                  placeholder="Your Business Name"
                  autoComplete="organization"
                />
                {errors.business && (
                  <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-red-500 text-sm">
                    {errors.business.message}
                  </motion.span>
                )}
              </div>

              {/* Message */}
              <div className="space-y-2">
                <label className="block text-sm font-semibold text-slate-900">
                  Message <span className="text-red-500">*</span>
                </label>
                <textarea
                  {...register('message', { required: 'Please tell us about your project' })}
                  className="input-field resize-none h-32"
                  placeholder="Tell us about your project, goals, and timeline..."
                />
                {errors.message && (
                  <motion.span initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-red-500 text-sm">
                    {errors.message.message}
                  </motion.span>
                )}
              </div>

              {/* Progress indicator */}
              <div className="flex items-center gap-2 px-4 py-3 bg-blue-50 rounded-lg">
                <div className="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                  <motion.div
                    animate={{ width: `${(filledFields / 6) * 100}%` }}
                    className="h-full bg-gradient-to-r from-blue-500 to-cyan-500"
                    transition={{ duration: 0.3 }}
                  />
                </div>
                <span className="text-xs font-medium text-slate-600">
                  {filledFields}/6 fields
                </span>
              </div>

              {/* Submit Button */}
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                type="submit"
                disabled={isSubmitting}
                className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isSubmitting ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="animate-spin">⌛</span>
                    Sending...
                  </span>
                ) : submitted ? (
                  <span className="flex items-center justify-center gap-2">
                    ✓ Message Sent Successfully!
                  </span>
                ) : (
                  'Send Message →'
                )}
              </motion.button>

              {/* Error message */}
              <AnimatePresence>
                {submitError && (
                  <motion.div
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    className="p-4 rounded-lg bg-red-50 border border-red-200 text-red-700 text-sm"
                  >
                    {submitError}
                  </motion.div>
                )}
              </AnimatePresence>

              {/* Success message */}
              <AnimatePresence>
                {submitted && (
                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: 10 }}
                    className="p-4 rounded-lg bg-green-50 border border-green-200"
                  >
                    <p className="font-semibold text-green-900 mb-1">Message sent successfully!</p>
                    <p className="text-sm text-green-700">
                      We'll be in touch within 24 hours. Check your email for confirmation.
                    </p>
                  </motion.div>
                )}
              </AnimatePresence>
            </form>
          </motion.div>
        </div>

        {/* Trust statement */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, margin: '0px 0px -100px 0px' }}
          transition={{ duration: 0.8 }}
          className="text-center text-slate-600 space-y-4"
        >
          <p className="text-sm font-medium">
            ✓ No spam  •  ✓ Quick response  •  ✓ No obligation  •  ✓ Free consultation
          </p>
          <p className="text-xs text-slate-500">
            By submitting, you agree to our privacy policy. We'll never share your information.
          </p>
        </motion.div>
      </div>
    </section>
  )
}
